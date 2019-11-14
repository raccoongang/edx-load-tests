import json
from locust import task
from base import LmsTasks
class XblocksTasks(LmsTasks):

    def on_start(self):
        super(XblocksTasks, self).on_start()
        self.auto_auth()
        self.enroll(self.course_id)
        self.survey_5_questions = {"enjoy": "Y", "recommend": "Y", "learn": "Y", "1571745947645": "Y", "1571745949501": "Y"}
        self.survey_10_questions = {"enjoy": "Y", "recommend": "Y", "learn": "Y", "1571746451731": "Y", "1571746457794": "Y",
                "1571746464711": "Y", "1571746469376": "Y", "1571746473810": "Y", "1571746478302": "Y", "1571746484319": "Y"}
        self.survey_20_questions = {"enjoy": "Y", "recommend": "Y", "learn": "Y", "1571746451731": "Y", "1571746457794": "Y",
                "1571746464711": "Y", "1571746469376": "Y", "1571746473810": "Y", "1571746478302": "Y", "1571746484319": "Y",
                "1571746551314": "Y", "1571746560789": "Y", "1571746566323": "Y", "1571746570836": "Y", "1571746581858": "Y",
                "1571746587035": "Y", "1571746591954": "Y", "1571746596934": "Y", "1571746601479": "Y", "1571746606156": "Y"}
        self.survey_30_questions = {"enjoy": "Y", "recommend": "Y", "learn": "Y", "1571746451731": "Y", "1571746457794": "Y",
                "1571746464711": "Y", "1571746469376": "Y", "1571746473810": "Y", "1571746478302": "Y", "1571746484319": "Y",
                "1571746551314": "Y", "1571746560789": "Y", "1571746566323": "Y", "1571746570836": "Y", "1571746581858": "Y",
                "1571746587035": "Y", "1571746591954": "Y", "1571746596934": "Y", "1571746601479": "Y", "1571746606156": "Y",
                "1571746646347": "Y", "1571746653102": "Y", "1571746657179": "Y", "1571746661954": "Y", "1571746665907": "Y",
                "1571746669996": "Y", "1571746673733": "Y", "1571746677874": "Y", "1571746716094": "Y", "1571746720953": "Y"}

    def _create_post_request(self, name, **kwargs):
        post_req = self.client.post(
            '/courses/course-v1:Andrey+670+2019/xblock/block-v1:Andrey+670+2019+type@survey+block@16b06dbb58244ccf8f13b3589d29cbbd/handler/vote',
            json.dumps(kwargs),
            headers=self.post_headers,
            name=name
        )
        return post_req

    @task(1)
    def test_survey_5_question(self):
        data = self.survey_5_questions
        response = self._create_post_request(
            'XBlock_5',
            **data
        )

    @task(1)
    def test_survey_10_question(self):
        data = self.survey_10_questions
        response = self._create_post_request(
            'XBlock_10',
            **data
        )

    @task(1)
    def test_survey_20_question(self):
        data = self.survey_20_questions
        response = self._create_post_request(
            'XBlock_20',
            **data
        )

    @task(1)
    def test_survey_30_question(self):
        data = self.survey_30_questions
        response = self._create_post_request(
            'XBlock_30',
            **data
        )