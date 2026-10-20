const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'}).catch(async()=>await chromium.launch());
const p=await b.newPage({viewport:{width:420,height:1400}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="margin:0;font-family:sans-serif">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const out=async(n)=>{const t=await p.evaluate(()=>[...document.querySelectorAll('#vv,.kpi')].map(e=>e.innerText.replace(/\n/g,' | ')).join(' || '));console.log(n,':',t)};
await out('two avg');await p.screenshot({path:'a.png',fullPage:true});
for(const l of ['one','L','U','isl']){await p.click(`[data-l="${l}"]`);await out(l)}
await p.click('[data-w="16"]');await out('isl couple');await p.click('[data-l="two"]');await out('two couple');
await p.click('summary');await p.check('#dh');await out('two couple dbl');
await p.fill('#cw','7');await p.fill('#cl','9');await out('check 7x9');
await p.click('[data-l="isl"]');await out('check isl 7x9');await p.click('[data-l="one"]');await out('check one 7x9');
await p.fill('#cw','5');await p.fill('#cl','5');await p.click('[data-w="5"]');await p.uncheck('#dh');await out('5x5 small one');await p.screenshot({path:'m.png',fullPage:true});
console.log('errors',errs);await b.close()})();
