import java.io.File;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;

// append text to an existing file

String fileTimePath = "text.txt";
FileWriter fw = null;
BufferedWriter bw = null;
PrintWriter pwOut = null;
try {
    fw = new FileWriter(fileTimePabw fferedWriter(fw);
    pwOut = new PrintWriter(bw);
    pwOut.println("the text");
    pwOut.close();
} catch (IOException e) {
    e.printStackTrace();
}
