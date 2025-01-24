# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book, Borrow, Users
from .serializers import BookSerializer, BorrowSerializer, UsersSerializer
from rest_framework import status
from django.http import HttpResponse

 

# Borrow Views

@api_view(['POST'])
def return_book(request):
    try:
        borrow_id = request.data.get('borrow_id')
        borrow_instance = Borrow.objects.get(id=borrow_id)
        borrow_instance.return_date = request.data.get('return_date')
        borrow_book.is_returned = True
        borrow_instance.calculate_penalty()
        borrow_instance.save()


        borrow_instance.book.available_copies += 1
        borrow_instance.book.save()

        return Response({"message": "Book returned successfully", "penalty": borrow_instance.penalty}, status=status.HTTP_200_OK)
    except Borrow.DoesNotExist:
        return Response({"error": "Borrow record not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def user_borrow_history(request, id):
    print(id)
    user=Users.objects.get(id=id)
    borrows = Borrow.objects.filter(user=user).order_by('-borrow_date')
    mylist=[]
    
    for i in borrows:

        descinary={}
        descinary['id']=i.id
        descinary['book_title']=i.book.title
        descinary['borrow_date']=i.borrow_date
        descinary['return_date']=i.return_date
        descinary['penalty']=i.penalty
        descinary['book']=i.book.id
        descinary['user']=i.user.id
        descinary['username']=i.user.username

        mylist.append(descinary)

    return Response(mylist)
    # serializer = BorrowSerializer(borrows, many=True)
    # return Response(serializer.data)


@api_view(['GET'])
def list_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_details(request):
    id=request.data.get("id" )
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)
@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['put'])
def edit_book(request,id):
    author=request.data.get("author" )
    available_copies=request.data.get("available_copies" )
    genre=request.data.get("genre" )
    publication_year=request.data.get("publication_year" )
    title=request.data.get("title" )
    try:
         book=Book.objects.get(id=id)
         book.author=author
         book.available_copies=available_copies
         book.genre=genre
         book.publication_year=publication_year
         book.title=title
         book.save()
         return Response(book.title, status=status.HTTP_201_CREATED)
    

    except:


        
        return Response("book does not exist", status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()   
        return Response({"message": "book deleted successfully."}, status=status.HTTP_200_OK)
    except Users.DoesNotExist:
        return Response({"error": "Library book not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def borrow_book(request):
    serializer = BorrowSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        book = serializer.validated_data['book']
        if book.available_copies > 0:
            book.available_copies -= 1
            book.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "No copies available"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def list_users(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def create_library_user(request):
    try:
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        statuss = request.data.get("status")
        role = request.data.get("role")
        
        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)
        user = Users.objects.create(username=username, password=password, email=email, status=statuss,role=role)

        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_library_user(request ):
    try:
        id=request.data.get("id" )
        library_user = Users.objects.get(id=id)

        username = request.data.get("username" )
        password = request.data.get("password")
        email = request.data.get("email")
        statuss = request.data.get("status")
        role = request.data.get("role")

        # Update username and password
        library_user.username = username
        library_user.email = email
        library_user.role = role
        library_user.status = statuss
        if password:
            library_user.password=password
        library_user.save()

        serializer = UsersSerializer(library_user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Users.DoesNotExist:
        return Response({"error": "Library user not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def auth(request ):
    try:

        username = request.data.get("username" )
        password = request.data.get("password")
        isadmin = request.data.get("isAdmin")
        role = "admin"
        if isadmin==True:
            role="admin"
        else:
            role="user"
        print(username,password,role,isadmin)


        try:
            user=Users.objects.get(username=username )
        except Users.DoesNotExist:
            return Response({"error": "Library user not found."}, status=status.HTTP_404_NOT_FOUND)

        if user.password==password and user.role==role:
            serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Users.DoesNotExist:
        return Response({"error": "Library user not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_library_user(request, id):
    try:
        library_user = Users.objects.get(id=id)
        library_user.delete()  # Deleting associated Django User also deletes the Users
        return Response({"message": "User deleted successfully."}, status=status.HTTP_200_OK)
    except Users.DoesNotExist:
        return Response({"error": "Library user not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def borrows(request):
    borrows = Borrow.objects.all()
    mylist=[]
    
    for i in borrows:

        descinary={}
        descinary['id']=i.id
        descinary['book_title']=i.book.title
        descinary['borrow_date']=i.borrow_date
        descinary['return_date']=i.return_date
        descinary['penalty']=i.penalty
        descinary['book']=i.book.id
        descinary['user']=i.user.id
        descinary['username']=i.user.username

        mylist.append(descinary)

    return Response(mylist)


