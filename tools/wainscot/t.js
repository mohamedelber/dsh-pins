const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const p=await b.newPage({viewport:{width:420,height:1500}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="margin:0;font-family:sans-serif">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const out=async(n,all)=>{const t=await p.evaluate((all)=>[...document.querySelectorAll(all?'#vv,.kpi,#tp li':'#vv,.kpi')].map(e=>e.innerText.replace(/\n/g,' | ')).join(' || '),all);console.log('\n#',n,':',t)};
await out('default',1);
for(const w of ['96','144','192']){await p.click(`[data-w="${w}"]`);for(const t of ['pf','pn','tw','bb']){await p.click(`[data-t="${t}"]`);await out(w+' '+t)}}
await p.click('[data-w="120"]');await p.click('[data-t="pf"]');await p.screenshot({path:'a.png',fullPage:true});
await p.click('summary');await p.fill('#ww','152');await p.selectOption('#gp','3.5');await p.selectOption('#tg','24');await out('A2D 152 3.5');
await p.fill('#ww','168');await p.selectOption('#gp','3');await out('TDC 168 3');
await p.fill('#hc','48');await out('halfway 48',1);
await p.fill('#hc','');await p.click('[data-t="pn"]');await p.selectOption('#hs','36');await out('panels 36',1);
await p.selectOption('#un','cm');await p.click('[data-t="tw"]');await out('cm tw',1);
await p.screenshot({path:'m.png',fullPage:true});
console.log('errors',errs);await b.close()})();
