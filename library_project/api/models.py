from django.db import models
from accounts.fields import CaseInsensitiveCharField

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Create your models here.
class Book(models.Model):
    """
    A model of the Books in the Library database
    """

    title = CaseInsensitiveCharField(max_length=70, blank=False, null=False, unique=True)
    author = CaseInsensitiveCharField(max_length=100, blank=False, null=False)
    ISBN = models.CharField(max_length=13, unique=True, blank=False)
    published_date = models.DateField(blank=True, null=True)
    book_copies = models.PositiveIntegerField(verbose_name='Number of Book Copies')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        pass

    # def validate_ISBN(self):
    #     pass

    def update_book_copies(self):
        """
        Run after post_save signal from CheckOut
        """
        self.book_copies = self.book_copies - 1
        return self.book_copies
    
    def update_book_copies_return(self):
        """
        run after delete signal from CheckOut
        """
        self.book_copies = self.book_copies + 1
        return self.book_copies

    class Meta:
        pass

class BookStatus(models.Model):
    """
    Keeps the status of a book in the library
    """
    class Status(models.IntegerChoices):
        available = 1
        not_available = 0

    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='book_status')
    status = models.PositiveSmallIntegerField(choices=Status)

    def update_checkout_status(self):
        """
        Updates the Book availability Status by checking the book copies
        """
        if self.book.book_copies >= 1:
           self.status = 1
        else:
            self.status = 0
        return self.status

        
    def save(self, *args, **kwargs):
        if self.status == None:
            self.status = self.update_checkout_status()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} status: {self.status}"
    
class CheckOut(models.Model):
    """
    Stores Information about the Book Borrowed Date it was Borrowed and Who borrowed it
    the return date is also going to be calculated later or something
    """

    user= models.ForeignKey(to=get_user_model(), on_delete=models.RESTRICT, related_name='user_checkouts')
    book = models.ForeignKey(to=BookStatus, on_delete=models.RESTRICT, related_name='books_checkout')
    checkout_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def can_checkout(self):
        if not self.book.status == 1:
            raise ValidationError('Sorry this book is not available at the Moment')

    def save(self, *args, **kwargs):
        self.can_checkout()
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # self.return_date = ''
        return super().delete(*args, **kwargs)

    def __str__(self):
        return f"Book: {self.book.book.title} checked out by {self.user.username} at {self.checkout_date}"
    
    class Meta:
        unique_together = ['user', 'book']
    
