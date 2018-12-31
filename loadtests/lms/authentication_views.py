from locust import task

from base import LmsTasks


class AuthenticationViewsTasks(LmsTasks):

    @task(9)
    def login_logout(self):
        """
        Test the primary login/logout endpoints.
        """

        """
        if self.locust._is_logged_in:
            self.logout()
        else:
            self.login_via_sso()
        """
        self.login_via_sso()

    @task(1)
    def stop(self):
        """
        Switch to a new TaskSet.
        """
        self.interrupt()
