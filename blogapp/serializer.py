from rest_framework import serializers
from blogapp.models import Blog, Category




class BlogSerializer(serializers.ModelSerializer):
    # ======> Serializer method field -> extra field <======
    len_blog_title = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = "__all__"

    def get_len_blog_title(self, object):
        return len(object.blog_title)
    
    # ======> Field-level validation <======
    def validate_blog_title(self, value):
        if value == "":
            raise serializers.ValidationError("Title must not be empty")
        elif len(value) < 4:
            raise serializers.ValidationError("Title is too short!")
        else:
            return value
        
    # ======> Object-level validation <======
    def validate(self, data):
        if data['blog_title'] == data["blog_description"]:
            raise serializers.ValidationError("Blog title and description can not be same.")
        else:
            return data
        
class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        exclude = ['id']
# --------------------------- simple serializer ----------------------------

# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     blog_title = serializers.CharField()
#     author = serializers.CharField()
#     blog_description = serializers.CharField()
#     post_date = serializers.DateField()
#     is_public = serializers.BooleanField()
#     slug = serializers.CharField()

#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)
    
#     def update(self,instance ,validated_data):
#         instance.blog_title = validated_data.get('blog_title', instance.blog_title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.blog_description = validated_data.get('blog_description', instance.blog_description)
#         instance.is_public = validated_data.get('is_public', instance.is_public)
#         instance.post_date = validated_data.get('post_date', instance.post_date)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.save()
#         return instance