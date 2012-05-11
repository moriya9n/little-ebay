from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
import pytz
from lebay.models import AuctionEvent
from lebay.constants import AUCTION_ITEM_STATUS_RUNNING
from lebay.utils import process_ended_auction

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        current_time = timezone.now()
        ended_auctions = AuctionEvent.objects.filter(end_time__lt=current_time, item__status=AUCTION_ITEM_STATUS_RUNNING)
        for auction_event in ended_auctions:
            process_ended_auction(auction_event)
