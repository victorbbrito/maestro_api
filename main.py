from typing import Literal
import requests

class MaestroApi():
    URL = "https://developers.botcity.dev/api/v2"
    
    def __init__(self, login:str, key:str) -> None:
        self.__login__ = login
        self.__key__ = key
        self.__access_token__ = self.get_maestro_api_access_token()
        self.__organization__ = None # vem junto com o access token
        self.headers = {
            "Authorization": f"Bearer {self.__access_token__}",
            "Content-Type": "application/json"
        }
    
    
    def get_maestro_api_access_token(self) -> str:
        data = {"login":f"{self.__login__}", "key":f"{self.__key__}"}
        request = requests.api.post(url=self.URL+"/workspace/login", json=data)

        if request.status_code == 200:
            print("Authorized")
            response = request.json()
            return response['accessToken']
        else:
            return f"Erro {request.status_code}"
        

    def get_bot_list(self) -> list:     
        request = requests.api.get(url=self.URL+"/bot", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
        
    
    def get_bot(self, bot_id:str, version:str) -> dict:
        request = requests.api.get(url=self.URL+f"/bot/{bot_id}/version/{version}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    
    
    def get_task_list(self) -> list:
        request = requests.api.get(url=self.URL+f"/task?size=50%page=0&sort=dateCreation&days=7", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
        
    
    def task_creator(self, automation_label:str, test:bool = True, parameters:dict = {}) -> dict:
        data = {
            "activityLabel":automation_label,
            "test":test,
            "parameters": parameters
        }
        request = requests.api.post(url=self.URL+f"/task", headers=self.headers, json=data)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
        
    
    def task_finisher(self, task_id:int,status:Literal["SUCCESS","FAILED"],message:str) -> dict:
        data = {
            "state": "FINISHED",
            "finishStatus": status,
            "finishMessage": message
        }

        request = requests.api.post(url=self.URL+f"/task/{task_id}", headers=self.headers, json=data)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    
    
    def task_restarter(self, task_id:int) -> dict:
        data = {
            "state": "START"
        }

        request = requests.api.post(url=self.URL+f"/task/{task_id}", headers=self.headers, json=data)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_task(self, task_id:int) -> dict:
        request = requests.api.get(url=self.URL+f"/task/{task_id}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    
    def delete_task(self, task_id:int) -> dict:
        request = requests.api.delete(url=self.URL+f"/task/{task_id}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_automation_list(self) -> list:
        request = requests.api.get(url=self.URL+f"/activity", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_automation(self, automation_label:str) -> dict:
        request = requests.api.get(url=self.URL+f"/activity/{automation_label}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
        
        
    def get_result_files_list(self)->list:
        request = requests.api.get(url=self.URL+f"/artifact?size=50%page=0&sort=dateCreation,desc&days=7", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
        
    
    def get_result_file_register(self, artifact_id:int):
        request = requests.api.get(url=self.URL+f"/artifact/{artifact_id}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_result_file(self, artifact_id:int):
        request = requests.api.get(url=self.URL+f"/artifact/{artifact_id}/file", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    
    
    def get_alerts(self)->list:
        request = requests.api.get(url=self.URL+f"/alerts?size=50%page=0&sort=dateCreation,desc&days=30", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code} - {request.text}"
    
    
    def get_warnings(self)->list:
        request = requests.api.get(url=self.URL+f"/alerts?type=WARN&size=50%page=0&sort=dateCreation,desc&days=60", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"


    def get_runner_metrics(self, runner_id:str):
        request = requests.api.get(url=self.URL+f"/machine/{runner_id}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_runner_log(self, runner_id:str) -> str:
        request = requests.api.get(url=self.URL+f"/machine/log/{runner_id}", headers=self.headers)
        
        if request.status_code == 200:
            return request.text

        else:
            return f"Erro {request.status_code}"
    
    
    def get_runner_tasks_summary(self, runner_id:str, days:int) -> list:
        request = requests.api.get(url=self.URL+f"/machine/{runner_id}/tasks-summary?days={days}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_all_schedules(self) -> list:
        request = requests.api.get(url=self.URL+f"/scheduling", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
        
    
    def delete_schedule(self, schedule_id:str) -> str:
        request = requests.api.delete(url=self.URL+f"/scheduling/{schedule_id}", headers=self.headers)
        
        if request.status_code == 200:
            return "Done"

        else:
            return f"Erro {request.status_code}"
    

    def schedule_creator(self, automation_label:str, cron:str, schedule_strategy:str, parameters:dict ,repository:str = "DEFAULT", active:bool = True, priority:int = 0) -> dict:
        
        data = {
            "activityLabel":automation_label,
            "organizationLabel":self.__organization__,
            "repositoryLabel":repository,
            "cron":cron,
            "scheduleStrategy": schedule_strategy,
            "parameters": parameters
        }

        request = requests.api.post(url=self.URL+f"/scheduling", headers=self.headers, json=data)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_credential_list(self) -> list:
        request = requests.api.get(url=self.URL+f"/credential", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_credential(self, credential_label:str) -> dict:
        request = requests.api.get(url=self.URL+f"/credential/{credential_label}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_credential_value(self, credential_label:str, credential_key:str) -> dict:
        request = requests.api.get(url=self.URL+f"/credential/{credential_label}/key/{credential_key}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
        
    
    def credential_creator(self, label:str, secrets:list[{"key","value"}], repository:str = "DEFAULT"):
        
        data = {
            "label": label,
            "organizationLabel" : self.__organization__,
            "secrets": secrets,
            "repositoryLabel":repository 
        }

        request = requests.api.post(url=self.URL+f"/credential", headers=self.headers, json=data)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_errors_list(self) -> list:
        request = requests.api.get(url=self.URL+f"/error", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
        
    
    def get_error(self, error_id:str) -> dict:
        request = requests.api.get(url=self.URL+f"/error", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    
    
    def get_error_by_automation(self, automation_label:str, days:int) -> dict:
        request = requests.api.get(url=self.URL+f"/error?automationLabel={automation_label}&days={days}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_datapool_list(self) -> list:
        request = requests.api.get(url=self.URL+f"/datapool", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def get_datapool(self, datapool_label:str) -> dict:
        request = requests.api.get(url=self.URL+f"/datapool/{datapool_label}", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"

    
    def get_datapool_view(self, datapool_label:str) -> dict:
        request = requests.api.get(url=self.URL+f"/datapool/{datapool_label}/view", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
        
    
    def get_datapool_summary(self, datapool_label:str) -> dict:
        request = requests.api.get(url=self.URL+f"/datapool/{datapool_label}/summary", headers=self.headers)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def datapool_creator(self, datapool_label:str, policy:str, auto_retry:bool, max_auto_retry:int, item_max_processing_time:int, trigger:str = "NEVER") -> list:

        data = {
            "label":datapool_label,
            "consumptionPolicy":policy,
            "autoRetry":auto_retry,
            "maxAutoRetry":max_auto_retry,
            "itemMaxProcessingTime": item_max_processing_time,
            "trigger":trigger
        }

        request = requests.api.get(url=self.URL+f"/datapool", headers=self.headers , json=data)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
    

    def datapool_add_item(self, datapool_label:str, priority:int, values:dict = {"product_name","product_category","product_value"}) -> dict:
        
        data = {
            "priority":priority,
            "values":values
        }

        request = requests.api.get(url=self.URL+f"/datapool/{datapool_label}/push", headers=self.headers , json=data)
        
        if request.status_code == 200:
            return request.json()

        else:
            return f"Erro {request.status_code}"
        

if __name__ == "__main__":


    # this information will available in developer enviroment in botcity maestro orchestrator
    data = {"login":"", "key":""}
    
    maestro = MaestroApi(data["login"],data["key"])

    #print(maestro.get_bot_list())
    #print(maestro.get_bot("test_bot","1"))
    #print(maestro.get_task_list())
    #print(maestro.task_creator("testelabel",True,{"is_test":1}))
    #print(maestro.task_finisher(4135503,"SUCCESS","Its works !"))
    #print(maestro.task_restarter(4135503))
    #print(maestro.get_task(4135503))
    #print(maestro.delete_task(4135503))
    #print(maestro.get_automation_list())
    #print(maestro.get_automation("testelabel"))
    #print(maestro.get_runner_log())


