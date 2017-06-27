select Users.first_name, Users.last_name, User2.first_name as Friend_first_name, User2.last_name as Friend_last_name
from Users
left join Friendships on Users.id = Friendships.User_id
left join Users as User2  on Friendships.friend_id = User2.id;
