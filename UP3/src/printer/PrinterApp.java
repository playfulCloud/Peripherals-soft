package printer;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.print.*;
import javax.swing.*;

public class PrinterApp implements Printable {
    private String textToPrint = "Tekst do wydrukowania fajne sobie testuje zajebisty soft do drukarki";
    private Font font = new Font("Arial", Font.PLAIN, 12);
    private Color textColor = Color.BLACK;
    private BufferedImage image = new BufferedImage(100, 100, BufferedImage.TYPE_INT_ARGB);
    private PageFormat pageFormat = new PageFormat();

    @Override
    public int print(Graphics g, PageFormat pf, int pageIndex) {
        if (pageIndex > 0) {
            return NO_SUCH_PAGE;
        }

        Graphics2D g2d = (Graphics2D) g;

        // Ustawienia strony
        g2d.translate(pf.getImageableX(), pf.getImageableY());
        g2d.setClip(0, 0, (int) pf.getImageableWidth(), (int) pf.getImageableHeight());

        // Ustawienia czcionki i koloru tekstu
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

    public void setPageFormat(PageFormat pageFormat) {
        this.pageFormat = pageFormat;
    }

    public static void main(String[] args) {
        PrinterApp app = new PrinterApp();

        // Ustawienia strony
        PageFormat pageFormat = new PageFormat();
        pageFormat.setOrientation(PageFormat.LANDSCAPE);
        Paper paper = pageFormat.getPaper();
        paper.setSize(600, 400); // Rozmiar strony (szerokość, wysokość)
        paper.setImageableArea(50, 50, 500, 300); // Marginesy (lewy, górny, szerokość, wysokość)
        pageFormat.setPaper(paper);
        app.setPageFormat(pageFormat);

        // Ustawienia czcionki
        Font font = new Font("Times New Roman", Font.BOLD, 16);
        app.setFont(font);

        // Ustawienia koloru tekstu
        Color textColor = Color.RED;
        app.setTextColor(textColor);

        // Ustawienia grafiki
        BufferedImage image = new BufferedImage(100, 100, BufferedImage.TYPE_INT_ARGB);
        Graphics2D g2d = image.createGraphics();
        g2d.setColor(Color.BLUE);
        g2d.fillRect(0, 0, 100, 100);
        app.setImage(image);

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
