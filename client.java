import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class client {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a sentence:");
        String input = scanner.nextLine();

        StringBuilder jsonBuilder = new StringBuilder();
        jsonBuilder.append("{");
        String[] words = input.split("\\s+");
        for (int i = 0; i < words.length; i++) {
            jsonBuilder.append("\"word").append(i).append("\": \"").append(words[i]).append("\"");
            if (i < words.length - 1) {
                jsonBuilder.append(",");
            }
        }
        jsonBuilder.append("}");

        try (FileWriter file = new FileWriter("data.json")) {
            file.write(jsonBuilder.toString());
            System.out.println("Data stored in data.json file");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
