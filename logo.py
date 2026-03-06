from PIL import Image, ImageDraw, ImageFont
import math

W, H = 800, 800
img = Image.new("RGBA", (W, H), (0,0,0,0))
draw = ImageDraw.Draw(img)

cx, cy = W//2, H//2

NAVY   = (10,25,60)
CYAN   = (0,180,230)
WHITE  = (255,255,255)
SILVER = (210,220,235)

# ---------- Outer Ring ----------
R_OUT, R_IN = 310, 265

draw.ellipse([cx-R_OUT,cy-R_OUT,cx+R_OUT,cy+R_OUT], fill=NAVY)
draw.ellipse([cx-R_IN,cy-R_IN,cx+R_IN,cy+R_IN], fill=(0,0,0,0))

# ---------- Inner Circle ----------
R_BG = 260
draw.ellipse([cx-R_BG,cy-R_BG,cx+R_BG,cy+R_BG], fill=NAVY)

# ---------- Fonts ----------
font_arc = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 30)
font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 48)
font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 30)

# ---------- Function to draw arc text ----------
def draw_arc_text(text, radius, start_angle, total_angle, inward=False):

    chars = list(text[::-1]) if inward else list(text)
    n = len(chars)

    for i,ch in enumerate(chars):

        frac = (i+0.5)/n
        angle = start_angle + frac*total_angle

        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)

        if inward:
            rot = math.degrees(angle) + 270
        else:
            rot = math.degrees(angle) + 90

        ch_img = Image.new("RGBA",(80,80),(0,0,0,0))
        ch_draw = ImageDraw.Draw(ch_img)

        w,h = ch_draw.textbbox((0,0),ch,font=font_arc)[2:4]
        ch_draw.text(((80-w)/2,(80-h)/2),ch,font=font_arc,fill=SILVER)

        ch_img = ch_img.rotate(-rot,expand=True)

        px = int(x - ch_img.width/2)
        py = int(y - ch_img.height/2)

        img.paste(ch_img,(px,py),ch_img)

# ---------- Top Arc ----------
draw_arc_text(
"AMAL JYOTHI COLLEGE OF ENGINEERING",
radius=235,
start_angle=math.radians(200),
total_angle=math.radians(140),
inward=False
)

# ---------- Bottom Arc ----------
draw_arc_text(
"• KANJIRAPALLY •",
radius=235,
start_angle=math.radians(20),
total_angle=math.radians(140),
inward=True
)

# ---------- Center Symbol < /> ----------
bx, by = cx, cy-20
lw = 10

draw.line([(bx-85,by),(bx-35,by-55)],fill=CYAN,width=lw)
draw.line([(bx-85,by),(bx-35,by+55)],fill=CYAN,width=lw)

draw.line([(bx+85,by),(bx+35,by-55)],fill=CYAN,width=lw)
draw.line([(bx+85,by),(bx+35,by+55)],fill=CYAN,width=lw)

draw.line([(bx-15,by+60),(bx+15,by-60)],fill=WHITE,width=lw)

# ---------- Center Text ----------
text = "CODING CLUB"
bbox = draw.textbbox((0,0),text,font=font_title)
tw = bbox[2]-bbox[0]

draw.text((cx-tw/2,cy+70),text,font=font_title,fill=WHITE)

draw.line([(cx-150,cy+130),(cx+150,cy+130)],fill=CYAN,width=3)

text2 = "OF AJCE"
bbox2 = draw.textbbox((0,0),text2,font=font_sub)
tw2 = bbox2[2]-bbox2[0]

draw.text((cx-tw2/2,cy+140),text2,font=font_sub,fill=SILVER)

# ---------- Save ----------
final = Image.new("RGB",(W,H),(255,255,255))
final.paste(img,mask=img.split()[3])

final.save("coding_club_logo.png",dpi=(300,300))
img.save("coding_club_logo_transparent.png",dpi=(300,300))

print("Logo generated.")
