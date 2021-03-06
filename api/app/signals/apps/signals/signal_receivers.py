from django.dispatch import receiver

from signals.apps.signals import tasks
from signals.apps.signals.managers import create_child, create_initial, update_status


@receiver(create_initial, dispatch_uid='signals_create_initial')
def signals_create_initial_handler(sender, signal_obj, **kwargs):
    tasks.translate_category(signal_obj.id)
    tasks.apply_routing(signal_obj.id)


@receiver(create_child, dispatch_uid='signals_create_child')
def signals_create_child_handler(sender, signal_obj, **kwargs):
    tasks.translate_category(signal_obj.id)


@receiver(update_status, dispatch_uid='signals_update_status')
def update_status_handler(sender, signal_obj, status, prev_status, *args, **kwargs):
    tasks.update_status_children_based_on_parent(signal_id=signal_obj.pk)
