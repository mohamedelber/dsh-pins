const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const OUT='/home/claude/dsh-pins/fetch/out/';
const pages={'home':'dailyspacehacks.com','post':'over-the-toilet-storage-ideas','cat':'kitchen-pantry-hacks'};
const D=process.argv[2];
(async()=>{const b=await chromium.launch();
for(const [w,h,tag] of [[1280,900,'desk'],[390,844,'mob']]){
 const c=await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:1,isMobile:tag==='mob'});
 await c.route('**/*',async r=>{const u=new URL(r.request().url());
   if(u.hostname!=='dailyspacehacks.com'){return r.abort()}
   let base=path.basename(u.pathname)||'';
   if(u.pathname==='/'){return r.fulfill({path:OUT+'dailyspacehacks.com',contentType:'text/html'})}
   if(u.pathname.endsWith('/')){const n=u.pathname.split('/').filter(Boolean).pop();if(fs.existsSync(OUT+n))return r.fulfill({path:OUT+n,contentType:'text/html'});return r.abort()}
   let f=OUT+base; if(!fs.existsSync(f)){const m=base.replace(/-\d+x\d+(\.\w+)$/,'$1');f=OUT+m}
   if(!fs.existsSync(f)){f=OUT+base.replace(/-\d+x\d+(\.\w+)$/,'-1$1')}
   if(fs.existsSync(f)){const ext=path.extname(f);const ct={'.css':'text/css','.js':'application/javascript','.jpg':'image/jpeg','.jpeg':'image/jpeg','.png':'image/png','.woff2':'font/woff2','.svg':'image/svg+xml','.webp':'image/webp'}[ext]||'application/octet-stream';return r.fulfill({path:f,contentType:ct})}
   return r.abort()});
 for(const [k,p] of Object.entries(pages)){const pg=await c.newPage();
  const url='https://dailyspacehacks.com/'+(k==='home'?'':(k==='cat'?'category/kitchen-pantry-hacks/':p+'/'));
  await pg.goto(url,{waitUntil:'load',timeout:30000}).catch(e=>console.log('goto',e.message));
  await pg.waitForTimeout(1500);
  await pg.evaluate(()=>{document.querySelectorAll('img[loading=lazy],img[data-lazyloaded],img[data-src]').forEach(i=>{if(i.dataset.src)i.src=i.dataset.src;if(i.dataset.srcset)i.srcset=i.dataset.srcset;i.loading='eager'})});
  await pg.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,120))}window.scrollTo(0,0)});await pg.waitForTimeout(1500);
  await pg.screenshot({path:`${D}/${k}-${tag}.png`,fullPage:true});
  const hgt=await pg.evaluate(()=>document.body.scrollHeight);console.log(k,tag,hgt);await pg.close()}
 await c.close()}
await b.close()})();
