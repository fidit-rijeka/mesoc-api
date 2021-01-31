from django.core.management import BaseCommand
from django.utils.timezone import now

from core.models import PasswordReset, Verification


class Command(BaseCommand):
    def handle(self, *args, **options):
        count_verification = Verification.objects.filter(expires_at__lte=now()).delete()[0]
        count_password_reset = PasswordReset.objects.filter(expires_at__lte=now()).delete()[0]

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully deleted {} verification and {} password reset requests.'.format(
                    count_verification,
                    count_password_reset
                )
            )
        )
