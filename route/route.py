from fastapi import APIRouter, File, UploadFile, HTTPException
from model.palette_gen import PaletteGenerator
from io import BytesIO
import scipy
from PIL import Image


def read_imagefile(file) -> Image:
    img = Image.open(BytesIO(file))
    print(img.height, img.width)
    return img


router = APIRouter()


@router.post("/upload")
async def create_upload_file(
    image: UploadFile = File(...),
):
    print(image.filename)
    extension = image.filename.split(".")[-1].lower() in ("jpg", "jpeg", "png")
    if not extension:
        raise HTTPException(
            status_code=422, detail="Image must be jpg or png format!")

    img = read_imagefile(await image.read())

    img = img.resize((200, 200), Image.ANTIALIAS)
    img = scipy.array(img)
    shape = img.shape
    img = img.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

    palette = PaletteGenerator()
    colors = palette.create_palette(img)

    return colors
