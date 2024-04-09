# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils import timezone

class Adminuser(models.Model):
    userid = models.OneToOneField('Allusers', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdminUser'


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('isadmin', True)

        return self.create_user(username, password, **extra_fields)

class Allusers(AbstractBaseUser, PermissionsMixin):
    userid = models.AutoField(db_column='UserID', primary_key=True)
    username = models.CharField(db_column='Username', max_length=255, unique=True)
    fname = models.CharField(db_column='FName', max_length=255, blank=True, null=True)
    lname = models.CharField(db_column='LName', max_length=255, blank=True, null=True)
    isadmin = models.BooleanField(db_column='IsAdmin', default=False)
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(default=timezone.now, null=True)
    is_superuser = models.BooleanField(default=False)  # Added is_superuser field

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions",
        related_query_name="user",
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        managed = True  # Be careful with this if you are managing the model manually
        db_table = 'AllUsers'

class Bidding(models.Model):
    biddingid = models.AutoField(db_column='BiddingID', primary_key=True)  # Field name made lowercase.
    buyerid = models.ForeignKey('Normaluser', models.DO_NOTHING, db_column='BuyerID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.ForeignKey('Item', models.DO_NOTHING, db_column='ItemID', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    biddingtime = models.TimeField(db_column='BiddingTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bidding'


class Cart(models.Model):
    cartid = models.AutoField(db_column='CartID', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey('Item', models.DO_NOTHING, db_column='ItemID', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Normaluser', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cart'


class Checkoutinformation(models.Model):
    checkoutid = models.AutoField(db_column='CheckoutID', primary_key=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Normaluser', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.
    preferredpayment = models.CharField(db_column='PreferredPayment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    edittime = models.TimeField(db_column='EditTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckoutInformation'


class Item(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    sellerid = models.ForeignKey('Normaluser', models.DO_NOTHING, db_column='SellerID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageURL', blank=True, null=True)  # Field name made lowercase.
    posteddate = models.DateField(db_column='PostedDate', blank=True, null=True)  # Field name made lowercase.
    startingprice = models.DecimalField(db_column='StartingPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    startingtime = models.TimeField(db_column='StartingTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Item'


class Message(models.Model):
    messageid = models.AutoField(db_column='MessageID', primary_key=True)  # Field name made lowercase.
    senderid = models.ForeignKey(Allusers, models.DO_NOTHING, db_column='SenderID', blank=True, null=True)  # Field name made lowercase.
    receiverid = models.ForeignKey(Allusers, models.DO_NOTHING, db_column='ReceiverID', related_name='message_receiverid_set', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Message'


class Normaluser(models.Model):
    userid = models.OneToOneField(Allusers, models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase.
    profile = models.CharField(db_column='Profile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    averagerating = models.DecimalField(db_column='AverageRating', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NormalUser'


class Notification(models.Model):
    notificationid = models.AutoField(db_column='NotificationID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(Allusers, models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemID', blank=True, null=True)  # Field name made lowercase.
    startingtime = models.DateTimeField(db_column='StartingTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notification'


class Ordertable(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    finalprice = models.DecimalField(db_column='FinalPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemID', blank=True, null=True)  # Field name made lowercase.
    buyerid = models.ForeignKey(Allusers, models.DO_NOTHING, db_column='BuyerID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deliverymethod = models.CharField(db_column='DeliveryMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    upsno = models.CharField(db_column='UPSNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderid1 = models.IntegerField(db_column='OrderID1', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderTable'


class Rating(models.Model):
    ratingid = models.AutoField(db_column='RatingID', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey(Ordertable, models.DO_NOTHING, db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    reviewerid = models.ForeignKey(Allusers, models.DO_NOTHING, db_column='ReviewerID', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rating'


class Upstracking(models.Model):
    trackingid = models.AutoField(db_column='TrackingID', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey(Ordertable, models.DO_NOTHING, db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    upsno = models.CharField(db_column='UPSNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UPSTracking'


