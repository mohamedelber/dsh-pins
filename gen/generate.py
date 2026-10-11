# Reads gen/*.json jobs: {"model":"gpt-image-2.5-sunburst","items":[...]}. Default model gpt-image-2.5-sunburst (cheaper than 1.5). Use quality high only for heroes.
# Skips items whose output already exists. Writes PNGs to gen/out/<job>/<name>.png
import json, os, glob, base64, urllib.request, time
key = os.environ.get("OPENAI_API_KEY")
log = open("gen/log.txt", "a")
def call(model, prompt, size, quality):
    body = json.dumps({"model": model, "prompt": prompt, "size": size, "quality": quality, "n": 1}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=body,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)
def edit(model, prompt, size, quality, path):
    import uuid
    b = uuid.uuid4().hex
    parts = []
    for k, v in (("model", model), ("prompt", prompt), ("size", size), ("quality", quality), ("n", "1")):
        parts.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    img = open(path, "rb").read()
    parts.append(f'--{b}\r\nContent-Disposition: form-data; name="image"; filename="in.png"\r\nContent-Type: image/png\r\n\r\n'.encode() + img + b"\r\n")
    parts.append(f"--{b}--\r\n".encode())
    req = urllib.request.Request("https://api.openai.com/v1/images/edits", data=b"".join(parts),
        headers={"Authorization": "Bearer " + key, "Content-Type": "multipart/form-data; boundary=" + b})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)
for jf in sorted(glob.glob("gen/*.json")):
    job = os.path.splitext(os.path.basename(jf))[0]
    spec = json.load(open(jf))
    os.makedirs(f"gen/out/{job}", exist_ok=True)
    for it in spec["items"]:
        out = f"gen/out/{job}/{it['name']}.png"
        if os.path.exists(out): continue
        model = it.get("model", spec.get("model", "gpt-image-2.5-sunburst"))
        try:
            if it.get("edit_from"):
                if not os.path.exists(it["edit_from"]):
                    log.write(f"{time.strftime('%F %T')} SKIP {job}/{it['name']} missing {it['edit_from']}\n"); continue
                res = edit(model, it["prompt"], it.get("size", "1024x1024"), it.get("quality", spec.get("quality", "medium")), it["edit_from"])
            else:
                res = call(model, it["prompt"], it.get("size", "1024x1024"), it.get("quality", spec.get("quality", "medium")))
            d = res["data"][0]
            if "b64_json" in d:
                open(out, "wb").write(base64.b64decode(d["b64_json"]))
            else:
                urllib.request.urlretrieve(d["url"], out)
            log.write(f"{time.strftime('%F %T')} OK {job}/{it['name']} {model} {it.get('quality')} usage={res.get('usage')}\n")
        except urllib.error.HTTPError as e:
            log.write(f"{time.strftime('%F %T')} ERR {job}/{it['name']} {e.code} {e.read()[:300]!r}\n")
        except Exception as e:
            log.write(f"{time.strftime('%F %T')} ERR {job}/{it['name']} {e!r}\n")
log.close()
