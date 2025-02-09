// C# Backend Calls SQL Server

public class EquipmentService
{
    private readonly AppDbContext _context;

    public EquipmentService(AppDbContext context)
    {
        _context = context;
    }

    public void CheckoutEquipment(int userId, int equipmentId)
    {
        var checkoutRecord = new CheckoutRecord
        {
            UserID = userId,
            EquipmentID = equipmentId,
            CheckoutDate = DateTime.Now
        };

        _context.CheckoutRecords.Add(checkoutRecord);
        _context.SaveChanges();
    }
}
