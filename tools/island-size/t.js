const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const p=await b.newPage({viewport:{width:420,height:1400}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="margin:0;font-family:sans-serif">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const out=async(n)=>{const t=await p.evaluate(()=>[...document.querySelectorAll('#vv,.kpi')].map(e=>e.innerText.replace(/\n/g,' | ')).join(' || '));console.log(n,':',t)};
for(const k of ['12x10','14x12','16x14','20x16']){await p.click(`[data-k="${k}"]`);for(const c of ['one','L','U']){await p.click(`[data-c="${c}"]`);await out(k+' '+c)}}
await p.screenshot({path:'a.png',fullPage:true});
await p.click('summary');await p.selectOption('#ai','48');await out('20x16 U 2cooks');
await p.selectOption('#un','m');await p.fill('#kl','5');await p.fill('#kw','4.2');await out('metric 5x4.2');
console.log('errors',errs);await b.close()})();
