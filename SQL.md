Use the example of SQL in Java and add an "AddUser" method inside the previous Datorium API project - User repository.
Try and run postman and verify with db browser that the data is there
COPY the code from today's lesson. Open the project with Controllers/Services/Repositories (we used it 2 weeks ago).
Open UserRepository
Inside add(User user) method, paste the code.

UserRepo.java
```
package com.datorium.Datorium.API.Repo;

import com.datorium.Datorium.API.DTO.User;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;

public class UserRepo {

    private ArrayList<User> users = new ArrayList<>();

    public int add(User user) {
        //users.add(user);
        //return users.size();
        users.add(user);
        String url = "jdbc:sqlite:my.db";
        try (var conn = DriverManager.getConnection(url)) {
            if (conn != null) {
                var statement = conn.createStatement();
                statement.execute("INSERT INTO people (name) VALUES ('" + user.name + "')");

                //INSERT INTO people (name) VALUES ('');DROP TABLE people;--')
            }
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
        return 0;
    }

    public ArrayList<User> getUsers() {
        return users;
    }

    public User update(int userIndex, User updateUserDTO){
        var user = users.get(userIndex);
        user.name = updateUserDTO.name;
        return user;
    }
}
```
Postman
![image](https://github.com/user-attachments/assets/a4151e8a-9f0e-4436-be77-00f34602c5af)

BD Browser for SQLite
![image](https://github.com/user-attachments/assets/78f7f66f-f685-4d0d-823a-67b203fa1163)




