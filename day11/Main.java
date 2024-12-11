import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<String> data = new ArrayList<String>(Arrays.stream(ReadFile().split("\\s+")).toList());
        for (int i = 0; i < 75; i++) {
            System.out.println(i);
            ArrayList<String> toAdd = new ArrayList<String>();
            for (int j = 0; j < data.size(); j++) {
                if (Long.parseLong(data.get(j)) == 0) {
                    data.set(j, "1");
                }
                else if (String.valueOf(Long.parseLong(data.get(j))).length() % 2 == 0) {
                    toAdd.add(String.valueOf(Long.parseLong(data.get(j))).substring(String.valueOf(Long.parseLong(data.get(j))).length() /2));
                    data.set(j,String.valueOf(Long.parseLong(data.get(j))).substring(0, String.valueOf(Long.parseLong(data.get(j))).length() /2));
                }
                else {
                    data.set(j,String.valueOf(Long.parseLong(data.get(j)) * 2024));
                }
            }
           data = new ArrayList<>(Stream.concat(data.stream(), toAdd.stream()).toList());
        }
        System.out.println(data.size());
    }

    public static String ReadFile() throws FileNotFoundException {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            String data = myReader.nextLine();
            myReader.close();
            return data;
    }
}
