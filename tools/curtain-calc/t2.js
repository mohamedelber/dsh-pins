const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
const cases=[['en-GB',{}],['en-GB',{wh:110}],['en-GB',{ww:180}],['en-US',{}],['en-GB',{ww:300,wh:200}]];
for(const [loc,vals] of cases){const c=await b.newContext({locale:loc});const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.cwd()+'/test.html');
for(const k in vals){await p.fill('#'+k,String(vals[k]));}
const t=await p.evaluate(()=>document.getElementById('vd').textContent+' || '+document.getElementById('by').innerText.replace(/\n+/g,' / '));
console.log(loc,JSON.stringify(vals),errs.join(';'),'\n  ',t);}
// sill and recess
const c=await b.newContext({locale:'en-GB'});const p=await c.newPage();await p.goto('file://'+process.cwd()+'/test.html');
await p.click('[data-l="sill"]');console.log('sill',await p.evaluate(()=>document.getElementById('vd').textContent+' || '+document.getElementById('by').innerText.replace(/\n+/g,' / ')));
await p.click('[data-m="in"]');console.log('recess',await p.evaluate(()=>document.getElementById('vd').textContent+' || '+document.getElementById('by').innerText.replace(/\n+/g,' / ')));
await p.click('[data-u="in"]');console.log('to inches',await p.evaluate(()=>document.getElementById('ww').value+' '+document.getElementById('vd').textContent));
await b.close();})();
