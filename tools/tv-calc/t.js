const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'}).catch(async()=>await chromium.launch());
for (const loc of ['en-US','en-GB']){
const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:800,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const r=async()=>p.evaluate(()=>['vv','kc','kb','kt','ks','ka'].map(i=>document.getElementById(i).textContent).join(' | '));
console.log(loc,'default:',await r());
await p.selectOption('#ts','75');console.log('75:',await r());
await p.fill('#ho',loc==='en-US'?'10':'25');console.log('bracket:',await p.textContent('#kbr'));
await p.check('#fp');console.log('fireplace:',await r());
await p.click('[data-s="bed"]');console.log('bed:',await r());
await p.click('[data-u="in"]');console.log('to in:',await r(), await p.inputValue('#eh'), await p.inputValue('#vd'));
await p.click('[data-u="cm"]');console.log('to cm:',await r(), await p.inputValue('#eh'), await p.inputValue('#vd'));
if(loc==='en-US'){await p.screenshot({path:'a.png',fullPage:true});await p.setViewportSize({width:380,height:900});await p.screenshot({path:'m.png',fullPage:true});}
console.log('errors',errs);await c.close();}
await b.close();})();
