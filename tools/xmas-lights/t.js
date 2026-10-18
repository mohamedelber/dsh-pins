const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const loc of ['en-GB','en-US']){
const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:800,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const r=async()=>p.evaluate(()=>['vv','kl','ks','ko','kg','kr'].map(i=>document.getElementById(i).textContent).join(' | '));
console.log(loc,'default:',await r());
await p.click('[data-h="9"]');console.log('9ft:',await r());
await p.click('[data-l="150"]');console.log('full:',await r());
await p.click('[data-h="4"]');console.log('4ft:',await r());
await p.click('summary');await p.click('[data-s="0.7"]');console.log('slim:',await r());
await p.selectOption('#ss','300');console.log('300:',await r());
await p.fill('#hx',loc==='en-GB'?'210':'7.5');console.log('custom:',await r());
await p.click('[data-u="'+(loc==='en-GB'?'ft':'m')+'"]');console.log('switch:',await r(),await p.inputValue('#hx'));
if(loc==='en-GB'){await p.screenshot({path:'a.png',fullPage:true});await p.setViewportSize({width:380,height:900});await p.screenshot({path:'m.png',fullPage:true});}
console.log('summary',await p.evaluate(()=>1));
console.log('errors',errs);await c.close();}
await b.close();})();
