from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import ReferalProgramAccount, Profile

@receiver(post_save, sender=Profile)
def update_referal_program_account(sender: type[Profile], instance: Profile, created: bool, **kwargs):
    if created and instance.referrer:
        ref = ReferalProgramAccount.objects.get(profile__pk=instance.referrer.pk)
        ref.referal_count += 1
        ref.save()
