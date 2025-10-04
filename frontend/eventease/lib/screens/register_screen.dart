import 'package:flutter/material.dart';
import '../api/api_service.dart';
import '../models/user.dart';
import 'login_screen.dart';
import 'package:fluttertoast/fluttertoast.dart';

class RegisterScreen extends StatelessWidget {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController fullNameController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final ApiService api = ApiService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Register")),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(controller: emailController, decoration: InputDecoration(labelText: "Email")),
            TextField(controller: fullNameController, decoration: InputDecoration(labelText: "Full Name")),
            TextField(controller: passwordController, decoration: InputDecoration(labelText: "Password"), obscureText: true),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text("Register"),
              onPressed: () async {
                bool success = await api.register(User(
                  email: emailController.text,
                  full_name: fullNameController.text,
                  password: passwordController.text,
                ));
                if (success) {
                  Fluttertoast.showToast(msg: "Registration Successful");
                  Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => LoginScreen()));
                } else {
                  Fluttertoast.showToast(msg: "Registration Failed");
                }
              },
            ),
          ],
        ),
      ),
    );
  }
}
