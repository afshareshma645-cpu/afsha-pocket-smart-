from fastapi import APIRouter
router = APIRouter()

@router.get('/test')
def test_planners():
    return {'msg': 'planners works'}
