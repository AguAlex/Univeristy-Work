import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        ArrayList<Student> students = new ArrayList<Student>();

        Student s1 = new Student("Animal", 123, 7.4);
        Student s2 = new Student("Jalbaaa", 234, 8.9);

        students.add(s1);
        students.add(s2);
        students.add(new Student("Miau miau", 233, 7.4));
        students.add(new Student("Mrrr paw", 233, 6.8));

        Collections.sort(students, new Comparator<Student>() {
            @Override
            public int compare(Student s1, Student s2) {
                return Double.compare(s1.getMedie(), s2.getMedie());
            }
        });


//        for (Student s : students) {
//            System.out.println(s);
//        }
//
//        System.out.println("Student cu medie cea mai mare: " + students.get(students.size() - 1));

        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        char firstChar = input.charAt(0);
        for (Student s : students) {
            if (s.getName().charAt(0) == firstChar) {
                System.out.println(s);
            }
        }


    }
}