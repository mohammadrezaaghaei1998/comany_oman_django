from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from translated_fields import TranslatedField
from django.utils.translation import gettext_lazy as _





class Brand(models.Model):
    name = TranslatedField(models.CharField(_('name'),max_length=200,null=True,blank=True))


    class Meta:
        verbose_name = _(' Brand')
        verbose_name_plural = _(' Brands')


    def __str__(self):
        return self.name


    
class Color(models.Model):
    name = TranslatedField(models.CharField(_('name'),max_length=200,null=True,blank=True))
    code = TranslatedField(models.CharField(_('code'),max_length=50,null=True,blank=True))    

    class Meta:
        verbose_name = _(' Color')
        verbose_name_plural = _(' Colors')


    def __str__(self):
        return self.name




class Categories (models.Model):
    name = TranslatedField(models.CharField(_('name'),max_length=200,null=True,blank=True))
    image = models.ImageField(_('image'),upload_to='product_images/img',null=True,blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return str(self.name) if self.name else f"Category {self.pk}"
    

class Subfield(models.Model):
    name = TranslatedField(models.CharField(_('name'),max_length=255))
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _(' Subfield')
        verbose_name_plural = _(' Subfields')

    def __str__(self):
        return str(self.name) if self.name else f"Subfield {self.pk}"
    


class Subfield_Item(models.Model):
    name = TranslatedField(models.CharField(_('name'),max_length=255))
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    subfield = models.ForeignKey(Subfield, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _(' Subfield_Item')
        verbose_name_plural = _(' Subfield_Items')


    def __str__(self):
        return str(self.name) if self.name else f"Subfield_Item {self.pk}"





class Product(models.Model):
    image = models.ImageField(_('image'),upload_to='product_images/img',null=True,blank=True)
    name = TranslatedField(models.CharField(_('name'),max_length=200,null=True,blank=True, default=None))
    price = models.DecimalField(_('price'),max_digits=6, decimal_places=2,null=True,blank=True, default=None)
    information = TranslatedField(models.TextField(_('information'),null=True,blank=True, default=None))
    description = TranslatedField(models.TextField(_('description'),null=True,blank=True, default=None))
    created_date = models.DateTimeField(default=timezone.now)
    origin = TranslatedField(models.CharField(_('origin'),max_length=255,null=True,blank=True, default=None))
    quantity = models.PositiveIntegerField(_('quantity'),null=True,blank=True, default=None)
    quality = TranslatedField(models.CharField(_('quality'),max_length=255,null=True,blank=True, default=None))


    subfield_item = models.ForeignKey(Subfield_Item,on_delete=models.CASCADE,null=True,blank=True, verbose_name=_('Subfield Item'))
    subfield = models.ForeignKey(Subfield,on_delete=models.CASCADE,null=True,blank=True, verbose_name=_('Subfield'))
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE,null=True,blank=True, verbose_name=_('Categories'))
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True, verbose_name=_('Brand'))
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True, verbose_name=_('Color'))
    discount_price = models.DecimalField(_('discount_price '),max_digits=10, decimal_places=2, null=True, blank=True)

    

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        
    def __str__(self):
        return str(self.name) if self.name else f"Product {self.pk}"




class Images(models.Model):
    image = models.ImageField(_('image'),upload_to='product_images/img',null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')







class Contact(models.Model):
    name = models.CharField(_('name'),max_length=255)
    email = models.EmailField(_('email'))
    message = models.TextField(_('message'))

    class Meta:
        verbose_name = _('Cntact')
        verbose_name_plural = _('Contacs')

    

    def __str__(self):
        return f"{self.name} - {self.email}"





class Collaboration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  
    product_name = TranslatedField(models.CharField(_('product name'),max_length=255, default=None))
    quantity = TranslatedField(models.PositiveIntegerField(_('quantity'), null=True, blank=True, default=None))
    quality = TranslatedField(models.CharField(_('quality'),max_length=255, default=None))
    origin = TranslatedField(models.CharField(_('origin'),max_length=255, default=None))
    description = TranslatedField(models.TextField(_('description'), default=None))
    product_images = TranslatedField(models.ImageField(upload_to='collaboration_images/', default='default_image.jpg'))
    whatsapp = models.CharField(_('whatsapp'),max_length=15, default=None)


    class Meta:
        verbose_name = _('Collaboration')
        verbose_name_plural = _('Collaborations')

    def __str__(self):
         return str(self.name) if self.name else f"Collaboration {self.pk}"

class CollaborationImage(models.Model):
    collaboration = models.ForeignKey(Collaboration, related_name='collaboration_images', on_delete=models.CASCADE)
    image = models.ImageField(_('image'),upload_to='collaboration_images/')

    class Meta:
        verbose_name = _(' CollaborationImage')
        verbose_name_plural = _(' CollaborationImages')


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='10000000000')
    name = models.CharField(_('name'),max_length=255, default=None)
    surname = models.CharField(_('surname'),max_length=255, default=None)
    email = models.EmailField(_('email'),max_length=255, unique=True, default=None)
    whatsapp = models.CharField(_('whatsapp'),max_length=15, default=None)
    country = models.CharField(_('country'),max_length=255, default=None)
    city = models.CharField(_('city'),max_length=255, default=None)
    company = models.CharField(_('company'),max_length=255, blank=True, null=True, default=None)


    class Meta:
        verbose_name = _(' UserInfo')
        verbose_name_plural = _(' UserInfos')

    def __str__(self):
        return self.email





class Investment(models.Model):
    name = TranslatedField(models.CharField(_('name'),max_length=100, default=None))
    profitability_percentage = models.DecimalField(_('profitability_percentage'),max_digits=5, decimal_places=2, default=None)
    duration_staying_money = models.IntegerField(_('duration_staying_money'),help_text='Duration in months', default=None)
    origin = TranslatedField(models.CharField(_('origin'),max_length=50, default=None))
    description = TranslatedField(models.TextField(_('description'),blank=True, null=True, default=None))
    start_date = models.DateField(_('start date'), default=None)
    end_date = models.DateField(_('end date'),blank=True, null=True, default=None)
    amount_invested = models.DecimalField(_('amount invested'),max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(_('image'),upload_to='investment_product/img',null=True,blank=True, default=None)


    class Meta:
        verbose_name = _(' Investment')
        verbose_name_plural = _(' Investments')

    def __str__(self):
         return str(self.name) if self.name else f"Investment {self.pk}"
    



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _(' Favorite')
        verbose_name_plural = _(' Favorite')

    def __str__(self):
        return f"{self.user.username}'s favorite - {self.investment.name}"


    


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = TranslatedField(models.CharField(_('name'),max_length=200, default=None))
    email = TranslatedField(models.EmailField(_('email'), default=None))
    address = TranslatedField(models.TextField(_('address'), default=None))
    phone_number = TranslatedField(models.CharField(_('phone number'),max_length=20, default=None))

    class Meta:
        verbose_name = _(' OrderProduct')
        verbose_name_plural = _(' OrderProducts')

    def __str__(self):
        # return f"Order for {self.product.name} by {self.user.username}"
        return str(self.name) if self.name else f"OrderProduct {self.pk}"
    



class OrderInvestment(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = TranslatedField(models.CharField(_('name'),max_length=200, default=None))
    email = TranslatedField(models.EmailField(_('email'), default=None))
    address = TranslatedField(models.TextField(_('address'), default=None))
    phone_number = TranslatedField(models.CharField(_('phone number'),max_length=20, default=None))

    class Meta:
        verbose_name = _(' OrderInvestment')
        verbose_name_plural = _(' OrderInvestments')

    def __str__(self):
        # return f"Order for {self.investment.name} by {self.user.username}"
        return str(self.name) if self.name else f"OrderInvestment {self.pk}"
    




class JobApplication(models.Model):
    name = models.CharField(_('name'),max_length=255, default=None)
    email =models.EmailField(_('email'), default=None)
    whatsapp_number = models.CharField(_('whatsapp number'),max_length=20, blank=True, null=True, default=None)
    country = models.CharField(_('country'),max_length=255, blank=True, null=True, default=None)
    city = models.CharField(_('city'),max_length=255, blank=True, null=True, default=None)
    cv = models.FileField(_('cv'),upload_to='cv/', blank=True, null=True, default=None)


    class Meta:
        verbose_name = _(' JobApplication')
        verbose_name_plural = _(' JobApplications')



    def __str__(self):
        return self.name





class Product_Assistance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product_name = models.CharField(_('product name'),max_length=255, default=None)
    quantity = models.PositiveIntegerField(_('quantity'), null=True, blank=True, default=None)
    quality = models.CharField(_('quality'),max_length=255, default=None)
    origin = models.CharField(_('origin'),max_length=255, default=None)
    description = models.TextField(_('description'), default=None)
    product_images = models.ImageField(_('product image'),upload_to='product_assistance_images/', default='default_image.jpg')
    whatsapp = models.CharField(_('whatsapp'),max_length=15, default=None)

    class Meta:
        verbose_name = _(' Product_Assistance')
        verbose_name_plural = _(' Product_Assistances')

    def __str__(self):
        return self.product_name

class Product_AssistanceImage(models.Model):
    product_assistance = models.ForeignKey(Product_Assistance, related_name='product_assistance_images', on_delete=models.CASCADE)
    image = models.ImageField(_('image'),upload_to='product_assistance_images/')


    class Meta:
        verbose_name = _(' Product_AssistanceImage')
        verbose_name_plural = _(' Product_AssistanceImages')


class Branches(models.Model):
    name = models.CharField(_('name'),max_length=255)
    country = models.CharField(_('country'),max_length=255)
    city = models.CharField(_('city'),max_length=255)
    email = models.EmailField(_('email'),max_length=255, unique=True, default='')
    number = models.CharField(_('number'),max_length=15, default='')
    address = models.CharField(_('address'),max_length=255)

    class Meta:
        verbose_name = _('Branch')
        verbose_name_plural = _('Branches')



class Team(models.Model):
    name =  TranslatedField(models.CharField(_('name'),max_length=255))
    job_title =  TranslatedField(models.CharField(_('job title'),max_length=255))
    description =  TranslatedField(models.TextField(_('description')))
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    googleplus_url = models.URLField(blank=True, null=True)
    pinterest_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    telegram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='team_members/', null=True, blank=True)

    def __str__(self):
        return self.name
