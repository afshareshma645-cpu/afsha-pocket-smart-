from fastapi import APIRouter
router = APIRouter()

@router.get('/test')
def test_session():
    return {'msg': 'session works'}
