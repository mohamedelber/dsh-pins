const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const loc of ['en-US','en-GB','en-AU','en-CA']){
const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:800,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const r=async()=>p.evaluate(()=>['vv','kr','kd','kp'].map(i=>document.getElementById(i).textContent).join(' | ')+' roll '+document.getElementById('rlw').value+'x'+document.getElementById('rll').value);
console.log(loc,'default:',await r());
await p.click('[data-p="64"]');console.log('large:',await r());
await p.click('summary');await p.selectOption('#pm','0.5');console.log('halfdrop:',await r());
await p.selectOption('#rs','61.5,10.05');console.log('615:',await r());
await p.click('[data-c="uk"]');console.log('toUK:',await r(),await p.inputValue('#ww'));
await p.click('[data-c="us"]');console.log('toUS:',await r(),await p.inputValue('#ww'));
console.log('errors',errs);await c.close();}
await b.close();})();
