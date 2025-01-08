from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from api.models import Book, CheckOut, BookStatus
from django.shortcuts import get_object_or_404

@receiver(post_save, sender=Book)
def create_book_status(sender, instance, created, **kwargs):
    if created:
        BookStatus.objects.create(book=instance)

@receiver(post_save, sender=Book)
def update_book_status(sender, instance, created, **kwargs):
    book_stat = BookStatus.objects.get(book=instance)
    book_stat.update_checkout_status()
    book_stat.save()


@receiver(post_save, sender=CheckOut)
def update_book_copies(sender, instance, created, **kwargs):
    if created:
        checked_out_book = instance.book.book.id
        book = Book.objects.get(id = checked_out_book)
        book.update_book_copies()
        book.save()
        book_stat = BookStatus.objects.get(book__id=book.id)
        book_stat.update_checkout_status()
        book_stat.save()

@receiver(post_delete, sender=CheckOut)
def update_book_copies_return(sender, instance, **kwargs):
    deleted_book = instance.book.book.id
    book = Book.objects.get(id=deleted_book)
    book.update_book_copies_return()
    book.save()
    book_stat = BookStatus.objects.get(book__id=book.id)
    book_stat.update_checkout_status()
    book_stat.save()