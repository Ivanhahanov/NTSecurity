from fastapi import APIRouter
import docker
import os, logging

dockers_history = list()
router = APIRouter()


@router.get('/static_analysis/check')
def check():
    return {'pwd': os.getcwd()}


@router.get('/run_task')
async def run_task():
    filename = os.listdir(f'{os.getcwd()}app/static_sandbox/files/')[1]
    answer = await run_container(filename)
    return {"answer": answer}


async def run_container(filename):
    client = docker.from_env()
    rules_path = os.getenv('RULES_PATH')
    malware_path = os.getenv('MALWARE_PATH')
    files_path = os.getenv('FILES_PATH')
    container = client.containers.run(image='blacktop/yara',
                                      remove=True,
                                      volumes={rules_path: {'bind': '/rules', 'mode': 'ro'},
                                               malware_path: {'bind': '/malware', 'mode': 'ro'},
                                               files_path: {'bind': '/files', 'mode': 'ro'}},
                                      command=['/rules/test.yar', '/rules/test2.yar', f'/files/{filename}'],
                                      detach=True)
    answer = container.logs()
    logging.info(answer)
    return check_answer(answer.decode())


def check_answer(answer):
    if answer:
        return [{'vulnerability': row.split()[0], 'filename': row.split()[1]} for row in answer.strip().split('\n')]
    else:
        return 'no malware detect'


@router.get('/history')
def get_history():
    return
