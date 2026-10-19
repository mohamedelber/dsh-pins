const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const loc of ['en-US','en-GB']){
const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:800,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const r=async()=>p.evaluate(()=>['vv','kn','kc','kb','kt'].map(i=>document.getElementById(i).textContent).join(' | '));
console.log(loc,'default:',await r());
await p.click('[data-w="sofa"]');console.log('sofa:',await r());
await p.click('#hts button:nth-child(5)');console.log('h5:',await r());
await p.click('[data-w="bed"]');console.log('bed:',await r());
await p.click('[data-w="mantel"]');console.log('mantel:',await r());
await p.click('summary');await p.fill('#fw','84');console.log('fw:',await p.evaluate(()=>document.getElementById('tp').textContent.slice(0,300)));
await p.click('[data-w="wall"]');await p.selectOption('#hk','3');console.log('wire:',await r());
await p.selectOption('#el','60');console.log('60:',await r());
await p.fill('#fh',loc==='en-US'?'72':'180');console.log('tall:',await r());
await p.selectOption('#hk','x');await p.fill('#hd','2');console.log('own:',await r());
await p.click('[data-u="'+(loc==='en-US'?'cm':'in')+'"]');console.log('switch:',await r(),await p.inputValue('#fh'));
if(loc==='en-US'){await p.fill('#fh','');await p.click('[data-w="sofa"]');await p.screenshot({path:'a.png',fullPage:true});await p.setViewportSize({width:380,height:900});await p.screenshot({path:'m.png',fullPage:true});}
console.log('errors',errs);await c.close();}
await b.close();})();
