import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
IAU="https://www.astro4edu.org/resources/glossary/term/378/"
KM="https://konmari.com/konmari-marie-kondo-tidy-challenge-week-two/"
p("A color coded closet is one of the simplest ways to make a wardrobe easier to use: when every shirt sits next to its closest color, you see what you own in seconds, spot the gaps and put things back without thinking. It also makes even a small, plain closet look calm and finished.")
p("This guide shows you the color coded closet order that works for most wardrobes, three ways to use it, a 7-step plan and 14 ideas for hanging clothes, folded clothes, drawers, small closets and shared closets, plus how to keep it from falling apart after a week.")
img(1)
summary(["<strong>Quick answer:</strong> Sort your clothes by category first, such as tops, pants and dresses, then hang each group from left to right: light neutrals, then red, orange, yellow, green, blue and purple, then dark neutrals. Use matching hangers, face every hook the same way and give new clothes a spot in their color.",
"Category first, then color, is the easiest system to keep.",
"Declutter before you sort, or you will color code clothes you never wear."],
"<strong>Time:</strong> 1 to 3 hours · <strong>Cost:</strong> free, or about $20 to $50 for matching hangers · <strong>Difficulty:</strong> Easy")
toc("color-coded-closet")
h2("The Color Coded Closet Order")
p("Most organizers use a version of the same order: light neutrals at one end, the colors of the rainbow in the middle and dark neutrals at the other end. It is easy to remember and it looks like one smooth gradient when the closet door is open.")
diagram(open('z.svg').read(),"The color coded closet order: light neutrals, then red, orange, yellow, green, blue and purple, then dark neutrals, plus three ways to use it.")
p(f"The rainbow part follows the visible spectrum. The IAU Office of Astronomy for Education's {ext(IAU,'glossary entry on the visible spectrum')} lists violet, indigo, blue, green, yellow, orange and red from shortest to longest wavelength, so hanging red to purple simply runs that list in reverse. If you prefer a light-to-dark look, Marie Kondo's {ext(KM,'closet tip in the KonMari tidy challenge')} suggests hanging longer, heavier items on the left and letting the colors get lighter as you move from left to right.")
h2("Rainbow, Light to Dark or Category First?")
table(["Method","How it works","Best for"],[
["Rainbow","Light neutrals, rainbow colors, dark neutrals","Colorful wardrobes"],
["Light to dark","One gradient from white to black, or the reverse","Mostly neutral wardrobes"],
["Category first","Tops, pants, dresses, then color inside each group","Busy people and small closets"],
["Color first","All blues together, whatever the type","Outfit planning by color"]])
p("If you are not sure, start with category first. You still get the color effect, but you never have to search a whole blue section for one pair of pants.")
h2("Quick Pick: Color Coded Closet Ideas by Closet")
table(["Your closet","Best ideas","Cost"],[
["Small reach-in closet","#1, #2, #12","Free to low"],
["Colorful wardrobe","#2, #3, #5","Free"],
["Mostly neutrals","#4, #12","Free"],
["Drawers and shelves","#7, #8, #9","Free to low"],
["Walk-in closet","#10, #6","Free"],
["Shared closet","#11, #2","Free"]])
h2("How to Color Code Your Closet in 7 Steps")
lst(["<strong>Declutter first.</strong> Take everything out and remove what you no longer wear, so you only sort clothes that stay.",
"<strong>Sort by category.</strong> Make piles for short tops, long tops, pants, skirts, dresses and jackets.",
"<strong>Choose your order.</strong> Rainbow, light to dark or category first; use the chart above.",
"<strong>Place the neutrals.</strong> Decide whether whites and creams start the row and greys and blacks end it, or the reverse.",
"<strong>Hang and fold by color.</strong> Work one category at a time, left to right.",
"<strong>Match the hangers.</strong> Use one hanger style and turn every hook the same way.",
"<strong>Keep a return rule.</strong> New and clean clothes go back into their color spot, not at the end of the rail."],True)
img(6)
p(f"If the closet is packed, do a full {a('closet-clean-out','closet clean out')} before you start; color coding works best when there is a little space between hangers.")
h2("Color Coded Closet Ideas for Hanging Clothes")
h3("1. Switch to Matching Slim Hangers")
p("Mixed hangers break up the color line and take more space. Slim matching hangers, in wood or velvet, make a color coded closet look even and leave room for more clothes. You do not need to buy them all at once; replace one category at a time.")
h3("2. Sort by Category First, Then by Color")
p("This is the classic method most organizers start with. Hang all short-sleeve tops together, then long-sleeve tops, then pants and dresses, and run the color order inside each group. It is the easiest version to keep tidy because you always know where a type of clothing lives.")
h3("3. Use Neutrals as Bookends")
p("Whites, creams and beiges at one end and greys, browns and black at the other frame the bright colors in the middle. Because most wardrobes have more neutrals than brights, this keeps the rainbow section short and easy to read.")
h3("4. Try the Rising-to-the-Right Look")
img(5)
p(f"For a mostly neutral wardrobe, hang long coats and dresses on the left and shorter pieces on the right, with the colors getting lighter from left to right. This is the arrangement Marie Kondo describes in her {ext(KM,'KonMari closet tip')}, and it gives a small closet a calm, ordered line.")
h3("5. Hang Prints With Their Main Color")
p("A striped or floral shirt goes with the color you notice first. If you have many prints, give them their own short section at the end of each category instead.")
h3("6. Split Each Color by Sleeve Length")
p("Inside each color, hang sleeveless, short-sleeve and long-sleeve pieces in that order. It is a small extra step that makes a big rail much faster to scan when you get dressed.")
h2("Color Coded Closet Ideas for Shelves and Drawers")
p("Color coding is not only for hanging clothes. Folded clothes and drawers often benefit even more, because you can see every item from above.")
h3("7. File-Fold T-Shirts by Color")
img(2)
p(f"Fold T-shirts into small rectangles and stand them upright in the drawer like files, sorted by color. You see every shirt at once and nothing gets buried. Our guide on {a('how-to-fold-clothes-to-save-space','how to fold clothes to save space')} shows the folds step by step.")
h3("8. Stack Sweaters by Color Family")
img(3)
p(f"On shelves, keep one color family per stack and add simple shelf dividers so the stacks stay straight. Keep stacks low enough to pull a sweater out without toppling the rest. If you need more shelves, see our {a('diy-closet-shelves','DIY closet shelves')} guide.")
h3("9. Sort Small Items Into Color Bins")
p("Socks, scarves, gym clothes and accessories are hard to color code piece by piece. Give each color family its own small bin or drawer section instead, so the overall look stays tidy without daily refolding.")
h2("Ideas for Walk-In, Small and Shared Closets")
h3("10. Run One Gradient Around a Walk-In")
img(4)
p(f"In a walk-in closet, start the color order at the door and let it flow around the room, so the gradient reads as one line. Put the colors you wear most at eye level near the entrance. Our {a('small-walk-in-closet-ideas','small walk-in closet ideas')} cover the layout.")
h3("11. Give Each Person Their Own Color Run")
p("In a shared closet, split the rail and give each person their own full color order. It avoids arguments about where things go and makes it obvious when one side is overflowing.")
h3("12. Keep a Short Color Palette in a Small Closet")
p(f"A small closet looks calmer with fewer colors. A wardrobe built around a few neutrals and two or three accent colors is easier to color code and easier to mix and match. Our {a('small-closet-organization-ideas','small closet organization ideas')} have more tips for tight spaces.")
h2("How to Keep a Color Coded Closet Tidy")
h3("13. Light the Closet Well")
p("Navy, black and dark green look the same in a dim closet. A bright LED light or a strip under the shelf helps you see the real colors and keeps the order correct when you put clothes away.")
h3("14. Give New Clothes a Spot Right Away")
p(f"Hang anything new in its color spot the day it arrives, and do a quick five-minute reset once a week. At each season change, swap clothes in and out but keep the same order. For the rest of the house, our guide on {a('how-to-declutter-your-home','how to declutter your home')} uses the same keep-it-simple rules.")
add(open('savebox.html').read())
h2("Common Color Coded Closet Mistakes")
lst(["<strong>Color coding before decluttering.</strong> You end up organizing clothes you never wear.",
"<strong>Ignoring categories completely.</strong> A pure color order can hide pants among shirts; sort by type first.",
"<strong>Mixing hanger styles.</strong> Uneven hangers break the color line and waste space.",
"<strong>Packing the rail too tightly.</strong> Leave a finger's width between hangers so you can see and return clothes.",
"<strong>Adding new clothes at the end.</strong> Always put them in their color spot."])
h2("Color Coded Closet FAQ")
h3("How do you organize your closet by color?")
p("To organize a closet by color, take everything out, declutter, then sort clothes by category. Inside each category, hang from left to right: light neutrals, red, orange, yellow, green, blue and purple, then dark neutrals. Use matching hangers and put new clothes in their color spot.")
h3("What is the best color order for a closet?")
p("The most common color coded closet order is white, cream and beige, then pink, red, orange, yellow, green, blue, navy and purple, then grey, brown and black. You can also reverse it, or use a simple light-to-dark gradient if your wardrobe is mostly neutral.")
h3("Should you organize clothes by color or by category?")
p("Do both: category first, then color. Grouping by type keeps clothes easy to find, and color order inside each group gives you the tidy look. Color first works if you plan outfits around colors, but it can scatter similar items across the rail.")
h3("Is a color coded closet worth it?")
p("For most people, yes. It takes one to three hours to set up, costs little or nothing and makes it faster to see what you own, find outfits and notice duplicates. The key is keeping a simple return rule so the order lasts.")
h2("Final Thoughts")
p("A color coded closet does not need new furniture or expensive organizers. Declutter, sort by category, pick an order and keep matching hangers, and your closet will look calm and work faster every morning.")
p(f"Want to keep going? See our ideas for {a('hat-storage-ideas','hat storage')}, {a('belt-storage-ideas','belt storage')} and {a('jewelry-storage-ideas','jewelry storage')}, and save this guide on Pinterest for your next closet reset.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<svg.*?</svg>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('color coded closet'),'code',txt.lower().count('color code'))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
