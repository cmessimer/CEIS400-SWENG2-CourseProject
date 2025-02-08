// C# API Receives the Request
[ApiController]
[Route("api/equipment")]
public class EquipmentController : ControllerBase
{
    private readonly EquipmentService _equipmentService;

    public EquipmentController(EquipmentService equipmentService)
    {
        _equipmentService = equipmentService;
    }

    [HttpPost("checkout")]
    public IActionResult CheckoutEquipment([FromBody] CheckoutRequest request)
    {
        _equipmentService.CheckoutEquipment(request.UserID, request.EquipmentID);
        return Ok(new { message = "Equipment checked out successfully." });
    }
}
