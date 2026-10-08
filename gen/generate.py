# Reads gen/*.json jobs: {"model":"gpt-image-1.5","items":[{"name":"x","prompt":"...","size":"1024x1024","quality":"medium"}]}
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
for jf in sorted(glob.glob("gen/*.json")):
    job = os.path.splitext(os.path.basename(jf))[0]
    spec = json.load(open(jf))
    os.makedirs(f"gen/out/{job}", exist_ok=True)
    for it in spec["items"]:
        out = f"gen/out/{job}/{it['name']}.png"
        if os.path.exists(out): continue
        model = it.get("model", spec.get("model", "gpt-image-1.5"))
        try:
            res = call(model, it["prompt"], it.get("size", "1024x1024"), it.get("quality", "medium"))
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
