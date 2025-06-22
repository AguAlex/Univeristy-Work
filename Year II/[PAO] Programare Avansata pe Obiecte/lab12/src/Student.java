public class Student {
    private String nume;
    private int grupa;
    private double medie;

    public Student(String nume, int grupa, double medie) {
        this.nume = nume;
        this.grupa = grupa;
        this.medie = medie;
    }

    public String getName() {
        return this.nume;
    }

    public double getMedie() {
        return this.medie;
    }

    @Override
    public String toString() {
        return "Student " + this.getName() + " cu medie " + this.getMedie();
    }
}
