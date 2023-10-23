package printer;

import java.awt.*;
import java.awt.print.*;
import javax.swing.*;
import java.awt.image.BufferedImage;

public class PrinterApp implements Printable {
    private String textToPrint = "Tekst do wydrukowania";
    private Font font = new Font("Arial", Font.PLAIN, 12);
    private Color textColor = Color.BLACK;
    private BufferedImage image = new BufferedImage(100, 100, BufferedImage.TYPE_INT_ARGB);

    @Override
    public int print(Graphics g, PageFormat pf, int pageIndex) {
        if (pageIndex > 0) {
            return NO_SUCH_PAGE;
        }

        Graphics2D g2d = (Graphics2D) g;
        g2d.translate(pf.getImageableX(), pf.getImageableY());

        // Ustawienie czcionki i koloru tekstu
        g2d.setFont(font);
        g2d.setColor(textColor);

        // Rysowanie tekstu
        g2d.drawString(textToPrint, 100, 100);

        // Rysowanie grafiki
        g2d.drawImage(image, 200, 200, null);

        return PAGE_EXISTS;
    }

    public void setFont(Font font) {
        this.font = font;
    }

    public void setTextColor(Color color) {
        this.textColor = color;
    }

    public void setImage(BufferedImage image) {
        this.image = image;
    }

    public static void main(String[] args) {
        PrinterApp app = new PrinterApp();

        PrinterJob job = PrinterJob.getPrinterJob();
        job.setPrintable(app);

        boolean doPrint = job.printDialog();
        if (doPrint) {
            try {
                job.print();
            } catch (PrinterException e) {
                e.printStackTrace();
            }
        }
    }
}
