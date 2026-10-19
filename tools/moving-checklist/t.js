const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const loc of ['en-US','en-GB','de-DE']){
const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:800,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const r=async()=>p.evaluate(()=>document.getElementById('vv').textContent+' | '+document.getElementById('pt').textContent+' | '+Array.from(document.querySelectorAll('.stg h4')).map(x=>x.textContent).join(' / '));
console.log(loc,'default:',await r());
await p.click('[data-h="o"]');console.log('own',await r());
for(const n of ['6','4','2','1']){await p.click('[data-t="'+n+'"]');console.log(n,await r())}
await p.click('summary');await p.fill('#md','2026-12-12');console.log('date',await r());
await p.check('#ok');await p.check('#op');await p.check('#of');console.log('kpf',await r());
await p.click('input[data-id]');await p.click('[data-t="8"]');console.log('tick',await r());
if(loc==='en-US'){await p.screenshot({path:'a.png',fullPage:true});await p.setViewportSize({width:380,height:900});await p.screenshot({path:'m.png',fullPage:true});
const t=await p.evaluate(()=>document.getElementById('ls').innerText);console.log(t)}
console.log('errors',errs);await c.close();}
await b.close();})();
