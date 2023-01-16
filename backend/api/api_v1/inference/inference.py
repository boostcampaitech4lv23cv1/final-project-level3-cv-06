import aiofiles

from utils import inference
from fastapi import APIRouter, HTTPException
from fastapi import FastAPI, File, UploadFile

router = APIRouter()


@router.post('/')
async def inference(img: UploadFile=File(...)):
    # TODO
    # predict 함수 수정 필요
    
    # 멀티 프로세스 혹은 멀티 쓰레드로 해야함
    # return 하고 나서 반환하도록 변경할 것
    # 사진 받아서 paint로 반환
    
    # async with aiofiles.open(out_file_path, 'wb') as out_file:
    #     while content := await in_file.read(1024):  # async read chunk
    #         await out_file.write(content)  # async write chunk
    try:
        async with aiofiles.open('./raw_image/test.jpg', 'wb') as out_file: # 받은 사진 저장
            content = await img.read()  # async read
            await out_file.write(content)  # async write
    except:
        return {"message": "There was an error makeing paint image"}
    finally:
        img.close()
        
    
    return {'test': 'success'}

    