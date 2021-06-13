class C
    def initialize(value)
        @value = value
    end

    def getValue()
        return @value
    end
    
    def show()
        p @value
    end
end

c1 = C.new(10)
# p c1.getValue()
c1.show()