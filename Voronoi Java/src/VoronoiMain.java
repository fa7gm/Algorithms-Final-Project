import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.WindowConstants;
public class VoronoiMain{

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String imagepath;
		imagepath = scan.nextLine();
		File file = new File(imagepath);
		try 
		{
			BufferedImage image = ImageIO.read(file);
		} 
		catch (IOException e) {

			System.out.println("Your image does not exist.");
		}
		
		JFrame window = new JFrame("Voronoi Painting");
		window.setSize(1000, 1500);
		window.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		window.setVisible(true);
	}
}
