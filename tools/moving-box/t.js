const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:820,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:780px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
for(const h of ['studio','1','2','3','4','5']){await p.click(`[data-h="${h}"]`);for(const a of ['0.7','1','1.35']){await p.selectOption('#amt',a);console.log(h,a,await p.textContent('#vd'),'|',await p.textContent('#k4e'));}}
await p.selectOption('#amt','1');await p.click('[data-h="studio"]');await p.fill('#liv','0');console.log('empty studio',await p.textContent('#vd'));
await p.click('[data-h="3"]');
await p.screenshot({path:'shot1.png',fullPage:true});
await p.setViewportSize({width:380,height:900});await p.screenshot({path:'shot2.png',fullPage:true});
console.log('errors',errs);await b.close();})();
