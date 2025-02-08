// C# Interacts with SQL Server
public class CheckoutRecord
{
    [Key]
    public int RecordID { get; set; }
    public int UserID { get; set; }
    public int EquipmentID { get; set; }
    public DateTime CheckoutDate { get; set; }
    public DateTime? ReturnDate { get; set; }
}
