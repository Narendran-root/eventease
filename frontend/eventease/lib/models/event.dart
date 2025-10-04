class Event {
  final int id;
  final String title;
  final String description;
  final String location;
  final String category;
  final DateTime date;
  final int capacity;

  Event({
    required this.id,
    required this.title,
    required this.description,
    required this.location,
    required this.category,
    required this.date,
    required this.capacity,
  });

  factory Event.fromJson(Map<String, dynamic> json) {
    return Event(
      id: json['id'],
      title: json['title'],
      description: json['description'],
      location: json['location'],
      category: json['category'],
      date: DateTime.parse(json['date']),
      capacity: json['capacity'],
    );
  }
}
