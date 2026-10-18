const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const loc of ['en-GB','en-US']){
const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:800,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const r=async()=>p.evaluate(()=>['vv','kr','kd','kp','kpe','ka'].map(i=>document.getElementById(i).textContent).join(' | '));
console.log(loc,'default:',await r());
await p.click('[data-p="64"]');console.log('large:',await r());
await p.click('[data-a="room"]');console.log('room:',await r());
await p.click('[data-p="0"]');console.log('room plain:',await r());
await p.fill('#wh',loc==='en-GB'?'9':'30');console.log('tall:',await r());
await p.fill('#wh',loc==='en-GB'?'2.4':'8');
await p.click('summary');await p.fill('#rp',loc==='en-GB'?'53':'21');console.log('rp:',await r());
await p.click('[data-u="'+(loc==='en-GB'?'ft':'m')+'"]');console.log('switch:',await r(),await p.inputValue('#ww'),await p.inputValue('#rlw'));
await p.fill('#ww','');console.log('empty:',await r());
if(loc==='en-GB'){await p.fill('#ww','3.5');await p.click('[data-u="m"]');await p.fill('#ww','3.5');await p.screenshot({path:'a.png',fullPage:true});await p.setViewportSize({width:380,height:900});await p.screenshot({path:'m.png',fullPage:true});}
console.log('errors',errs);await c.close();}
await b.close();})();
