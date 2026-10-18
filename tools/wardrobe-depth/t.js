const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'}).catch(async()=>await chromium.launch());
for (const loc of ['en-GB','en-US']){
const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:800,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const r=async()=>p.evaluate(()=>['vv','kr','km','kh'].map(i=>document.getElementById(i).textContent).join(' | '));
console.log(loc,'default:',await r());
await p.click('[data-d="sliding"]');console.log('sliding:',await r());
await p.click('[data-c="shelf"]');console.log('shelf:',await r());
await p.click('[data-c="hang"]');await p.click('summary');
for (const v of (loc==='en-GB'?['75','58','45','25']:['30','22','14'])){await p.fill('#hv',v);console.log('have',v,':',await r());}
await p.click('[data-u="'+(loc==='en-GB'?'in':'cm')+'"]');console.log('switch:',await r(),await p.inputValue('#hv'));
if(loc==='en-GB'){await p.screenshot({path:'a.png',fullPage:true});await p.setViewportSize({width:380,height:900});await p.screenshot({path:'m.png',fullPage:true});}
console.log('errors',errs);await c.close();}
await b.close();})();
