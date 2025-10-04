class User {
  final String email;
  final String full_name;
  final String password;

  User({required this.email, required this.full_name, required this.password});

  Map<String, dynamic> toJson() => {
        "email": email,
        "full_name": full_name,
        "password": password,
      };
}
