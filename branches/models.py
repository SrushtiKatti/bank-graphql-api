
from django.db import models

class Bank(models.Model):
    """
    Bank model to store bank information.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    """
    Branch model to store bank branches.
    """
    branch = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=20)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')

    def __str__(self):
        return f"{self.branch} ({self.ifsc})"
