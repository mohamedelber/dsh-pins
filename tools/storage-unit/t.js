const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const loc of ['en-GB','en-US']){
const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:800,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const r=async()=>p.evaluate(()=>['vv','kb','ka','ks','kse'].map(i=>document.getElementById(i).textContent).join(' | '));
console.log(loc,'default:',await r());
for(const w of ['0','1','2','4','5','6','car']){await p.click('[data-w="'+w+'"]');console.log(w,await r());}
await p.click('[data-w="4"]');await p.click('[data-q="0.5"]');console.log('half 3bed:',await r());
await p.click('summary');await p.check('#ai');console.log('aisle:',await r());
await p.click('[data-u="'+(loc==='en-GB'?'us':'uk')+'"]');console.log('switch:',await r());
if(loc==='en-GB'){await p.screenshot({path:'a.png',fullPage:true});await p.setViewportSize({width:380,height:900});await p.screenshot({path:'m.png',fullPage:true});}
console.log('errors',errs);await c.close();}
await b.close();})();
