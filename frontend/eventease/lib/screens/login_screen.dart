import 'package:flutter/material.dart';
import '../api/api_service.dart';
import 'home_screen.dart';
import 'register_screen.dart';
import 'package:fluttertoast/fluttertoast.dart';

class LoginScreen extends StatelessWidget {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final ApiService api = ApiService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Login")),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(controller: emailController, decoration: InputDecoration(labelText: "Email")),
            TextField(controller: passwordController, decoration: InputDecoration(labelText: "Password"), obscureText: true),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text("Login"),
              onPressed: () async {
                final token = await api.login(emailController.text, passwordController.text);
                if (token != null) {
                  Fluttertoast.showToast(msg: "Login Successful");
                  Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => HomeScreen()));
                } else {
                  Fluttertoast.showToast(msg: "Invalid credentials");
                }
              },
            ),
            TextButton(
              child: Text("Register"),
              onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => RegisterScreen())),
            ),
          ],
        ),
      ),
    );
  }
}
